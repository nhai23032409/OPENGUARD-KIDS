import uvicorn
from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_db, Base

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="OpenGuard Kids - Week 1")
templates = Jinja2Templates(directory="server/templates")

@app.on_event("startup")
def seed_data():
    db = next(get_db())
    if not db.query(models.Parent).filter_by(username="phuhuong").first():
        demo_parent = models.Parent(username="phuhuong", password="Demo@2026")
        db.add(demo_parent)
        db.commit()
        db.refresh(demo_parent)
        
        demo_device = models.Device(id="demo-device-001", name="Demo Device", parent_id=demo_parent.id)
        db.add(demo_device)
        db.commit()
        print("[seed] Created demo account: phuhuong / Demo@2026")
        print("[seed] Created demo device: demo-device-001")

@app.post("/heartbeat", response_model=schemas.HeartbeatResponse)
def heartbeat(data: schemas.HeartbeatCreate, db: Session = Depends(get_db)):
    hb = models.Heartbeat(
        device_id=data.device_id,
        status=data.status,
        policy_version=data.policy_version
    )
    db.add(hb)
    db.commit()
    
    return schemas.HeartbeatResponse(
        status="ok",
        policy_version=1,
        commands=[]
    )

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    parent = db.query(models.Parent).filter_by(username=username, password=password).first()
    if not parent:
        return RedirectResponse(url="/login", status_code=303)
    
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="session", value=username)
    return response

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    session = request.cookies.get("session")
    if not session:
        return RedirectResponse(url="/login")
    
    devices = db.query(models.Device).all()
    device_status = []
    for d in devices:
        last_hb = db.query(models.Heartbeat).filter_by(device_id=d.id).order_by(models.Heartbeat.timestamp.desc()).first()
        device_status.append({
            "id": d.id,
            "name": d.name,
            "last_seen": last_hb.timestamp if last_hb else "Never",
            "status": last_hb.status if last_hb else "offline"
        })
    
    return templates.TemplateResponse(request=request, name="dashboard.html", context={"username": session, "devices": device_status})

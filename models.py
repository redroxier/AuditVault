from sqlalchemy import Column, String, DateTime
from db import Base
from datetime import datetime


class Project(Base):
    __tablename__ = "projects"

    project_id = Column(String, primary_key=True)
    tenant_id = Column(String, nullable=False)


class Document(Base):
    __tablename__ = "documents"

    document_id = Column(String, primary_key=True)
    tenant_id = Column(String, nullable=False)
    project_id = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    sha256_hash = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, order_details):
    db_order_details = models.OrderDetail(
        amount=order_details.amount,
        order_id = order_details.order_id,
        sandwich_id = order_details.sandwich_id
    )
    db.add(db_order_details)
    db.commit()
    db.refresh(db_order_details)
    return db_order_details


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_details_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details_id).first()


def update(db: Session, order_details_id, order_details):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details_id)
    update_data = order_details.model_dump(exclude_unset=True)
    db_order_details.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_details.first()


def delete(db: Session, order_details_id):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details_id)
    db_order_details.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

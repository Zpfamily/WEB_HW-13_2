from datetime import date, timedelta

from sqlalchemy.orm import Session

from src.schemas import ContactModel,ContactFavoriteModel
from src.database.models import Contact, User


# async def get_contacts(db: Session, user: User, skip: int, limit: int, favorite: bool|None = None):
#     query = db.query(Contact)
#     if favorite is not None:
#         query = query.filter_by(Contact.user_id==user.id)
#     contacts = query.offset(skip).limit(limit).all()
#     return contacts


# async def get_contact_by_id(contact_id: int, user: User, db: Session):
#     contact = db.query(Contact).filter_by(Contact.id==contact_id, Contact.user_id==user.id).first()
#     return contact


# async def get_contact_by_email(email: str, user: User, db: Session):
#     contact = db.query(Contact).filter_by(email==email, Contact.user_id==user.id).first()
#     return contact


# async def create(body: ContactModel, user: User, db: Session):
#     contact = Contact(**body.model_dump())
#     contact.user_id = user.id
#     db.add(contact)
#     db.commit()
#     db.refresh(contact)
#     return contact


# async def update(contact_id: int, body: ContactModel, user: User, db: Session):
#     contact = await get_contact_by_id(contact_id, user, db)
#     if contact:
#         contact.first_name = body.first_name
#         contact.last_name = body.second_name
#         contact.email = body.email
#         contact.phone = body.phone
#         contact.birthday = body.birthday
#         contact.comments = body.comments
#         contact.favorite = body.favorite
#         db.commit()
#     return contact


# async def favorite_update(contact_id: int, body: ContactModel, db: Session):
#     contact = await get_contact_by_id(contact_id, db)
#     if contact:
#         contact.favorite = body.favorite
#         db.commit()
#     return contact


# async def delete(contact_id: int, db: Session):
#     contact = await get_contact_by_id(contact_id, db)
#     if contact:
#         db.delete(contact)
#         db.commit()
#     return contact


# async def search_contacts(param: dict, db: Session):
#     query = db.query(Contact)
#     first_name = param.get("first_name")
#     last_name = param.get("last_name")
#     email = param.get("email")
#     if first_name:
#         query = query.filter(Contact.first_name.ilike(f"%{first_name}%"))
#     if last_name:
#         query = query.filter(Contact.last_name.ilike(f"%{last_name}%"))   
#     if email:
#         query = query.filter(Contact.email.ilike(f"%{email}%"))   
#     contacts = query.offset(param.get("skip")).limit(param.get("limit"))
#     return contacts


# async def search_birthday(param: dict, db: Session):
#     days:int = int(param.get("days", 7)) + 1
#     filter_afetr = date.today()
#     filter_before = date.today() + timedelta(days = days)
#     query = db.query(Contact)
#     query = query.filter(Contact.birthday > filter_afetr, Contact.birthday <= filter_before)
#     contacts = query.offset(param.get("skip")).limit(param.get("limit"))
#     return contacts

# from datetime import date, timedelta

# from sqlalchemy.orm import Session

# from src.shemas.contact import ContactFavoriteModel, ContactModel
# from src.database.models import Contact


async def get_contacts(db: Session, user_id: int,  skip: int, limit: int, favorite: bool|None = None):
    query = db.query(Contact).filter_by(user_id=user_id)
    if favorite is not None:
        query = query.filter_by(user_id=user_id)
    contacts = query.offset(skip).limit(limit).all()
    return contacts


async def get_contact_by_id(contact_id: int, user_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id, user_id=user_id).first()
    return contact


async def get_contact_by_email(email: str, user_id: int, db: Session):
    contact = db.query(Contact).filter_by(email=email, user_id=user_id).first()
    return contact


async def create(body: ContactModel, user_id: int, db: Session):
    contact = Contact(**body.model_dump())
    contact.user_id = user_id
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update(contact_id: int, body: ContactModel, user_id: int, db: Session):
    contact = await get_contact_by_id(contact_id, user_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.comments = body.comments
        contact.favorite = body.favorite
        db.commit()
    return contact


async def favorite_update(contact_id: int, body: ContactFavoriteModel, user_id: int, db: Session):
    contact = await get_contact_by_id(contact_id, user_id, db)
    if contact:
        contact.favorite = body.favorite
        db.commit()
    return contact


async def delete(contact_id: int, user_id: int, db: Session):
    contact = await get_contact_by_id(contact_id, user_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def search_contacts(param: dict, user_id: int, db: Session):
    query = db.query(Contact).filter_by(user_id=user_id)
    first_name = param.get("first_name")
    last_name = param.get("last_name")
    email = param.get("email")
    if first_name:
        query = query.filter(Contact.first_name.ilike(f"%{first_name}%"))
    if last_name:
        query = query.filter(Contact.last_name.ilike(f"%{last_name}%"))   
    if email:
        query = query.filter(Contact.email.ilike(f"%{email}%"))   
    contacts = query.offset(param.get("skip")).limit(param.get("limit"))
    return contacts


async def search_birthday(param: dict, user_id: int, db: Session):
    days:int = int(param.get("days", 7)) + 1
    filter_afetr = date.today()
    filter_before = date.today() + timedelta(days = days)
    query = db.query(Contact).filter_by(user_id=user_id)
    query = query.filter(Contact.birthday > filter_afetr, Contact.birthday <= filter_before)
    contacts = query.offset(param.get("skip")).limit(param.get("limit"))
    return contacts
from sqlalchemy.orm import Session
from shared.models import Part, Location, Supplier
from typing import List, Optional

class PartRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_part(self, part_id: int) -> Optional[Part]:
        return self.db.query(Part).filter(Part.id == part_id).first()

    def get_all_parts(self) -> List[Part]:
        return self.db.query(Part).all()

    def create_part(self, part_data: dict) -> Part:
        part = Part(**part_data)
        self.db.add(part)
        self.db.commit()
        self.db.refresh(part)
        return part

    def update_part(self, part_id: int, part_data: dict) -> Optional[Part]:
        part = self.get_part(part_id)
        if part:
            for key, value in part_data.items():
                setattr(part, key, value)
            self.db.commit()
            self.db.refresh(part)
        return part

    def delete_part(self, part_id: int) -> bool:
        part = self.get_part(part_id)
        if part:
            self.db.delete(part)
            self.db.commit()
            return True
        return False 
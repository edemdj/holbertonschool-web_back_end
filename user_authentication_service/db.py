#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Save the user to the database """
        session = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds the first user that matches the given filters.
        """
        session = self._session

        valid_columns = User.__table__.columns.keys()

        for key in kwargs.keys():
            if key not in valid_columns:
                raise InvalidRequestError(f"Invalid column name: {key}")

        user = session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound("No user found matching the criteria.")

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates the attributes of a user identified by user_id.
        """
        session = self._session

        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise NoResultFound("No user found with the given ID.")

        valid_columns = User.__table__.columns.keys()

        for key, value in kwargs.items():
            if key not in valid_columns:
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)

        session.commit()

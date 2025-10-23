from typing import Generator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import settings
 

# block for interaction with database: 

# create async engin for interaction with database
engine = create_async_engine(settings.REAL_DATABASE_URL, future=True, echo=True)

# create session for the interaction with database
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
   """Dependecy for getting async session"""
   try:
      session: AsyncSession = async_session()
      yield session
   finally:
      await session.close()
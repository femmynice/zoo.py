{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "84b35e80-70ed-431e-991a-a86909fbd248",
   "metadata": {},
   "outputs": [],
   "source": [
    "# zoo.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3d6ed9e7-450d-475b-84bd-baf4d1b765d4",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "incomplete input (2017541953.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[2], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    def hours():\u001b[0m\n\u001b[1;37m                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m incomplete input\n"
     ]
    }
   ],
   "source": [
    "def hours():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f9ddf499-8a4d-4bc4-85eb-9b5bc14ffc97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Open 9-5 daily\n"
     ]
    }
   ],
   "source": [
    "print('Open 9-5 daily')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f0fa326-144a-4c5e-9e16-7b2dde653b2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import zoo as menagerie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "600975ce-d9bc-403d-9669-3dfda9eb2165",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'menagerie' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[12], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m menagerie\u001b[38;5;241m.\u001b[39mhours()\n",
      "\u001b[1;31mNameError\u001b[0m: name 'menagerie' is not defined"
     ]
    }
   ],
   "source": [
    "menagerie.hours()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76893b43-bc82-4703-be7c-b22b88908909",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4efeecfb-7d45-4d3f-ab51-2ecb83efac85",
   "metadata": {},
   "outputs": [],
   "source": [
    "from zoo import hours"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "15531734-c7d5-4a6e-b006-ae9f3ee90814",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'library' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[13], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m library(zoo)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'library' is not defined"
     ]
    }
   ],
   "source": [
    "library(zoo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5e04d62-2495-41ec-98ba-63b21542dc76",
   "metadata": {},
   "outputs": [],
   "source": [
    "hours()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b37c8bb-111b-4477-a6a3-d2e3e22c057d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63e90a39-a0f0-443d-b954-1a872e888a3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import create_engine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5944021-ba92-4681-b46a-e391e2989926",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine('sqlite:///books.db')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb473b4b-8cf6-4d6a-a914-a1f271604670",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import Table, Column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2419ee6-bac5-4ec6-9777-a65f7dcde853",
   "metadata": {},
   "outputs": [],
   "source": [
    "books = Table('book', metadata, autoload=True, autoload_with=engine)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71faa183-c949-4a01-8211-4f0fb7d8adcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "query = select([books.columns.title]).order_by(books.columns.title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f581bf33-f54a-4562-bb54-fa60bf5a8e20",
   "metadata": {},
   "outputs": [],
   "source": [
    "with engine.connect() as conn:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0068c155-d97d-47d7-ade0-58ba4033c92d",
   "metadata": {},
   "outputs": [],
   "source": [
    " result = conn.execute(query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb5b397f-6bbf-4ccb-9d50-145a9e9a2de2",
   "metadata": {},
   "outputs": [],
   "source": [
    "for row in result:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a43a029-5f27-4cf5-8434-24c786697e8f",
   "metadata": {},
   "outputs": [],
   "source": [
    " print(row['title'])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

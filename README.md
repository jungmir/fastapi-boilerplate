# Starting Guide

- ## Installation
    - ### Optional
        - install python-venv and execute venv
            - `pip install python-venv`
            - `python -m venv venv`
            ### Linux or MacOS
            - `source venv/bin/activate`
            ### Window
            - `source venv/script/activate`

    - ### Required
        - install postgresql >= 14.0
            ```
            psql postgres
            create user ${input id} with password ${input password}
            alter role ${user id} createdb
            ```
        - Write alembic.ini
            ```
            line 53
            sqlalchemy.url = postgresql://{user_id}:{user_password}@localhost/{db_name}
            ```
        - Write .env
            ```
            cp .env.example .env
            ```
        - install python >= 3.7
        - install python package
            - `pip install -r requirements.txt`

- ## Build
    - working directory: /codepia
    - database migration
        - `alembic upgrade head`
    - run server
        - `uvicorn server.main:app --host 0.0.0.0 --port 8080`
        - or
        - `python server/main.py`

- ## Start
    - access http://localhost:8080/docs

- ## Test
    - working directory: /codepia
    - `pytest`

- ## Directory tree
```
.
├── README.md
├── alembic.ini
├── pytest.ini
├── requirements.txt
├── server
│   ├── assets
│   │   └── schemas
│   │       ├── post.py
│   │       └── user.py
│   ├── common
│   │   ├── const.py
│   │   └── create_app.py
│   ├── database
│   │   ├── connection.py
│   │   └── models
│   │       ├── mixin
│   │       │   ├── activerecord.py
│   │       │   ├── base.py
│   │       │   ├── eagerload.py
│   │       │   ├── inspection.py
│   │       │   ├── repr.py
│   │       │   ├── serialize.py
│   │       │   ├── session.py
│   │       │   ├── smartquery.py
│   │       │   ├── timestamp.py
│   │       │   └── utils.py
│   │       └── user.py
│   ├── main.py
│   ├── migrations
│   │   ├── README
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       └── 638c68488b1c_create_user_table.py
│   ├── router
│   │   └── index.py
│   └── utils
└── tests
    ├── conftest.py
    └── test_api.py
```

- ## Ref
    - git [absent1706/sqlalchemy-mixins](https://github.com/absent1706/sqlalchemy-mixins)
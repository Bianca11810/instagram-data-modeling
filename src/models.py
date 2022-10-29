from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }
class Follower (Base):
    __tablename__ = "Follower"
    id = Column(Integer, primary_key = True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class User (Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key = True)
    username = Column(String(256))
    firstname = Column(String(256))
    lastname = Column(String(256))
    email = Column(String(256))

class Post (Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media (Base):
    __tablename__ = "Media"
    id = Column(Integer, primary_key = True)
    mediatype = Column(String(256))
    url = Column(String(256))
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment (Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key = True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('user.id'))


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e





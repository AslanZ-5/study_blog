from django.test import TestCase
from blog.models import Post, Comment
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(username='admin',password='test12345')
        self.user_2 = User.objects.create_user(username='aslan',password='test12345')
        self.post_1 = Post.objects.create(author=self.user_1,title='test post',body='my test post')
        self.comment_1 = Comment.objects.create(writer=self.user_1,post=self.post_1,content='good post')
        self.comment_2 = Comment.objects.create(writer=self.user_2,post=self.post_1,content='i agree with you',parent=self.comment_1)
        for i in range(1,7+1):
            a = User.objects.create_user(username=f'user{i}',password='test12345')
            b = Post.objects.create(title=f'post has been created by {a.username}',author=a,body='random text for post {i}')
            Comment.objects.create(writer=a,post=b,content=f'this is test comment by {a} for post {b}')
            self.post_1.likes.add(a)

        
    


    def test_user_password(self):
        checked = self.user_1.check_password('test12345')
        self.assertTrue(checked)
            
    def test_count_users_posts_and_comments(self):
        users_quantity = User.objects.all().count() 
        posts_quantity = Post.objects.all().count()
        comments_quantity = Comment.objects.all().count()
        self.assertTrue(users_quantity,9) 
        self.assertTrue(posts_quantity,8) 
        self.assertTrue(comments_quantity,9) 

    def test_comment(self):
        parent = self.comment_2.parent
        self.assertEqual(self.comment_1,parent)
        self.assertEqual(self.comment_1.id,1)
    
    def test_user_post_reverse_count(self):
        user = self.user_1
        qs = Post.objects.filter(author=user)
        self.assertEqual(qs.count(),1)

    def test_post_fields(self):
        field = self.post_1._meta.get_field('title').max_length
        self.assertEqual(field,220)
    def test_post_coments_count(self):
        post = self.post_1
        qs = post.comment_set.all().count()
        self.assertEqual(qs,2)

    def test_likes(self):
        likes = self.post_1.likes.count()
        self.assertEqual(likes,7)

    def test_post_str_method(self):
        d = self.post_1
        self.assertTrue(isinstance(d,Post))
        self.assertEqual(str(d),'Post "test post"')

    def test_post_get_absolute_url_method(self):
        a = self.post_1.get_absolute_url()
        post_tag = self.post_1.title_tag
        response = self.client.get(f'/post/{post_tag}/')
        self.assertEqual(a,f'/post/{post_tag}/')
        self.assertEqual(response.status_code,200)
        
#py manage.py test blog.tests.test_models
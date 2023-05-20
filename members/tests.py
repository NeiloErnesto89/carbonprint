from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse # reverse url lookup


# auth test example - https://www.youtube.com/watch?v=FLVB_HruIjk

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register') # here we are using the name of the url in the urls.py file
        self.login_url = reverse('login')
        # here we create the user object in dictionary format
        self.user = {
            'email': 'test@gmail.com', 
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'joe',
            'last_name': 'bloggs'}
        # self.user_bad_password = {'email': 'test@gmail.com', 
        #     'username': 'test2',
        #     'password1': '',
        #     'password2': 'a',
        #     'first_name': 'tony',
        #     'last_name': 'tot'}
            
        return super().setUp() # call the super class setUp method
    
class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url) # get the register page
        self.assertEqual(response.status_code, 200) # check if the page is loading correctly
        self.assertTemplateUsed(response, 'authenticate/register_user.html') # check if the correct template is used - PASSED
        
    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302) # check if the page is loading correctly via redirect which is 302 - PASSING
        
        
    # test to try and FAIL to register user with a short password
    # def test_cannot_register_user_with_bad_password(self):
    #     response = self.client.post(self.register_url, self.user_bad_password, format='text/html')
    #     self.assertEqual(response.status_code, 404) # check if the page is not loading via 400, as in the user has not been created - TEST PASSING  

class LoginTest(BaseTest): # access to the base test class
    def test_can_access_page(self):
        response = self.client.get(self.login_url) # via base test class
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')
           
        # can user login correctly
    def test_can_login_user_successfully(self):
        response = self.client.post(self.register_url, self.user, format='text/html') # register the user first
        # want to check if the user is logged in
        # user = User.objects.get(username=self.user['username']) # get the user object
        # user1 = User.objects.filter(username=self.user['username']).exists() # check if the user exists
        user = User.objects.filter(email=self.user['email']).first() # check if the user exists via email using first() method to return the first object
        # user = User.objects.create_user(username="test2", password="test2", email="test@two.com")
        user.is_active = True # set the user to active
        user.save() # save the user to 'db' - this is a test db
        response = self.client.post(self.login_url, self.user, format='text/html') # login the user via the login url and the user object
        self.assertEqual(response.status_code, 302) # check if the login page is loading correctly via redirect which is 302 - PASSING
        
    # def test_cannot_login_user_with_bad_password(self):
    #     response = self.client.post(self.register_url, self.user, format='text/html') # register the user first
    #     # now login the user with a bad password/unverifed user
    #     response = self.client.post(self.login_url, self.user, format='text/html') # login the user via the login url and the user object
    #     self.assertEqual(response.status_code, 400)

    # def test_cannot_login_user_with_bad_password(self):
    #     response = self.client.post(self.login_url, {'password': 'password'}, format='text/html') # post with no username
    #     self.assertEqual(response.status_code, 302) # no username supplied so should fail
    #     self.assertTemplateUsed(response, 'authenticate/login.html')
        
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="test1", password="test1", email="test@test.com")
        User.objects.create_user(username="test2", password="test2", email="test@two.com")
        
    def test_user(self):
        user1 = User.objects.get(username="test1")
        self.assertEqual(user1.email, "test@test.com") 
        # self.assertEqual(user1.password, "test1") # password is hashed so this will fail

class TestViews(TestCase):
    
    def test_login_redirect_unknown_user(self):
        # response = self.client.get('/authenticate/login/')
        # self.assertRedirects(response, '/login/')
        response = self.client.post('/authenticate/login/', {'username': 'unknown', 'password': 'unknown'})
        # self.assertRedirects(response, '/login/')
        self.assertEqual(response.status_code, 404)
        # self.assertTemplateUsed(response, 'registration/login.html')
        
       
        
     # test is admin has permission using Request Factory()
    # def test_admin_permission(self):
    #     admin_user = User.objects.create(email='admin@gmail.com',password='admin997',is_staff=True)
    #     factory = RequestFactory()
    #     request = factory.get('/')
    #     request.user = admin_user
    #     permission = user.is_staff
    #     has_permission = permission.has_permission(request, None)
    #     self.assertTrue(has_permission)
    




    # def test_register_user(self):
    #     request = self.factory.post('/register/', self.form_data) # mock object
    #     response = register_user(request)

    #     # Check that the user is redirected to the home page
    #     self.assertEqual(response.status_code, 200) # success via 200
    #     # print(response.url )
    #     # self.assertEqual(response.url, 'home_page')  # Replace '/home/' with your actual home page URL

    #     # Check that the user is created and logged in
    #     user = User.objects.get(username='test')
    #     self.assertTrue(user.is_authenticated)
    #     self.assertFalse(user.is_staff)

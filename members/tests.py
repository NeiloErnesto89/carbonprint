from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
# Create your tests here.

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

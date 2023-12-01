from django.test import SimpleTestCase
# Create your tests here.
class TestFrontTimes(SimpleTestCase):
    def test_front_times(self):
        response = self.client.get("/warmup-2/font-times/?n=2&input_str=Chocolate")
        self.assertContains(response, 'ChoCho')
    def test_front_times_2(self):
        response = self.client.get("/warmup-2/font-times/?n=3&input_str=Chocolate")
        self.assertContains(response, 'ChoChoCho')
    def test_front_times_3(self):
        response = self.client.get("/warmup-2/font-times/?n=3&input_str=Abc")
        self.assertContains(response, 'AbcAbcAbc')

class TestNoTeenSum(SimpleTestCase):
    def test_no_teen_sum(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=1&b=2&c=3")
        self.assertContains(response, 6)
    def test_no_teen_sum_2(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=13&c=1")
        self.assertContains(response, 3)
    def test_no_teen_sum_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=1&c=14")
        self.assertContains(response, 3)
        
class TestXYZThere(SimpleTestCase):
    def test_xyz_there(self):
        response = self.client.get("/string-2/xyz-there/?input_string=abcxyz")
        self.assertContains(response, True)
    def test_xyz_there_2(self):
        response = self.client.get("/string-2/xyz-there/?input_string=abc.xyz")
        self.assertContains(response, False)
    def test_xyz_there_3(self):
        response = self.client.get("/string-2/xyz-there/?input_string=xyz.abc")
        self.assertContains(response, True)

class TestCenteredAverage(SimpleTestCase):
    def test_centered_average(self):
        response = self.client.get("/list-2/centered-average/?nums1=3&nums2=5&nums3=1")
        self.assertContains(response, 3.0)
    def test_centered_average_2(self):
        response = self.client.get("/list-2/centered-average/?nums1=10&nums2=3&nums3=22")
        self.assertContains(response, 10.0)
    def test_centered_average_3(self):
        response = self.client.get("/list-2/centered-average/?nums1=15&nums2=2&nums3=1")
        self.assertContains(response, 2.0)
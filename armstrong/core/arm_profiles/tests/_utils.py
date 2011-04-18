from django.test import TestCase as DjangoTestCase
from django.test.client import RequestFactory

def generate_random_image():
    title = "Random Image %d" % random.randint(1000000, 2000000)
    url = "http://example.com/%d" % random.randint(1000000, 2000000)
    return Image.objects.create(title=title, url=url)

class TestCase(DjangoTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def assertInContext(self, var_name, other, template_or_context):
        # TODO: support passing in a straight "context" (i.e., dict)
        context = template_or_context.context_data
        self.assertTrue(var_name in context,
                msg="`%s` not in provided context" % var_name)
        self.assertEqual(context[var_name], other)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from quiz_app.api.serializers import QuestionSerializer
from quiz_app.models import Question

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):

	permission_classes = (IsAuthenticated)
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

	def get_queryset(self):
		query_params = self.request.GET.get('question')
		if query_params:
			queryset = self.request.user.questions.filter(is_private=False,
														  title__contains=query_params)
		else:
			queryset = self.request.user.questions.filter(is_private=False)

		return queryset
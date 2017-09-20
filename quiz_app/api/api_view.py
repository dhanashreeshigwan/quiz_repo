from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from quiz_app.api.serializers import QuestionSerializer
from quiz_app.models import Question
from quiz_app.api.permissions import IsApiKeyProvided
from quiz_app.api.tenant_throtling import TenantThrottle

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, IsApiKeyProvided)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    throttle_classes = (TenantThrottle)

    def get_queryset(self):
		query_params = self.request.GET.get('question')
		if query_params:
			queryset = self.request.user.questions.filter(is_private=False,
														  title__contains=query_params)
		else:
			queryset = self.request.user.questions.filter(is_private=False)

		return queryset
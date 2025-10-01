"""API endpoints for AI powered features."""
from __future__ import annotations

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

<<<<<<< HEAD
from .services import AiSuggestionClientError, AiSuggestionError, AiSuggestionService
=======
from .services import AiSuggestionError, AiSuggestionService
>>>>>>> 7ad07fbb72f48a4bb9603622b9ff1ee8bc7dc865


class SeoSuggestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        payload = request.data
        service = AiSuggestionService()
        try:
            suggestions = service.generate_seo_suggestions(
                title=payload.get("title", ""),
                summary=payload.get("summary", ""),
                content=payload.get("content", ""),
            )
<<<<<<< HEAD
        except AiSuggestionClientError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AiSuggestionError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
=======
        except AiSuggestionError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 7ad07fbb72f48a4bb9603622b9ff1ee8bc7dc865
        return Response(
            {
                "suggestions": [
                    {
                        "heading": suggestion.heading,
                        "description": suggestion.description,
                        "keywords": suggestion.keywords,
                        "risks": suggestion.risks,
                    }
                    for suggestion in suggestions
                ]
            }
        )

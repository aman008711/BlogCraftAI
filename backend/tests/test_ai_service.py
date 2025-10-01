from __future__ import annotations

<<<<<<< HEAD
import json

import httpx
import pytest

from ai.services import AiSuggestionClientError, AiSuggestionError, AiSuggestionService, SeoSuggestion
=======
import httpx
import pytest

from ai.services import AiSuggestionError, AiSuggestionService, SeoSuggestion
>>>>>>> 7ad07fbb72f48a4bb9603622b9ff1ee8bc7dc865


class DummyResponse:
    def __init__(self, json_data: dict, status_code: int = 200):
        self._json_data = json_data
        self.status_code = status_code
        self.request = httpx.Request("POST", "https://example.com")

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise httpx.HTTPStatusError("error", request=self.request, response=self)


class DummyClient:
    def __init__(self, response: DummyResponse | Exception):
        self.response = response

    def post(self, *args, **kwargs):
        if isinstance(self.response, Exception):
            raise self.response
        return self.response

    def close(self):  # pragma: no cover - not used directly
        pass


<<<<<<< HEAD
def _wrap_payload(payload: dict) -> dict:
    return {
        "candidates": [
            {
                "content": {
                    "parts": [
                        {"text": json.dumps(payload)}
                    ]
                }
            }
        ]
    }


@pytest.mark.django_db
def test_generate_seo_suggestions_success():
    response_payload = {
        "suggestions": [
            {
                "heading": "Optimise title",
                "description": "Add more keywords",
                "keywords": ["ai", "blog"],
                "risks": ["Verify statistics"],
            }
        ]
    }
    response = DummyResponse(_wrap_payload(response_payload))
=======
@pytest.mark.django_db
def test_generate_seo_suggestions_success():
    response = DummyResponse(
        {
            "suggestions": [
                {
                    "heading": "Optimise title",
                    "description": "Add more keywords",
                    "keywords": ["ai", "blog"],
                    "risks": ["Verify statistics"],
                }
            ]
        }
    )
>>>>>>> 7ad07fbb72f48a4bb9603622b9ff1ee8bc7dc865
    service = AiSuggestionService(client=DummyClient(response))
    suggestions = service.generate_seo_suggestions(
        title="AI Post",
        summary="Summary",
        content="Content",
    )
    assert suggestions[0] == SeoSuggestion(
        heading="Optimise title",
        description="Add more keywords",
        keywords=["ai", "blog"],
        risks=["Verify statistics"],
    )


@pytest.mark.django_db
def test_generate_seo_suggestions_timeout():
    client = DummyClient(httpx.TimeoutException("timeout"))
    service = AiSuggestionService(client=client)
    with pytest.raises(AiSuggestionError):
        service.generate_seo_suggestions(title="A", summary="B", content="C")


@pytest.mark.django_db
def test_generate_seo_suggestions_validation_error():
<<<<<<< HEAD
    response = DummyResponse(_wrap_payload({"unexpected": []}))
=======
    response = DummyResponse({"unexpected": []})
>>>>>>> 7ad07fbb72f48a4bb9603622b9ff1ee8bc7dc865
    service = AiSuggestionService(client=DummyClient(response))
    with pytest.raises(AiSuggestionError):
        service.generate_seo_suggestions(title="A", summary="B", content="C")


@pytest.mark.django_db
def test_build_payload_requires_fields():
<<<<<<< HEAD
    service = AiSuggestionService(client=DummyClient(DummyResponse(_wrap_payload({"suggestions": []}))))
    with pytest.raises(AiSuggestionClientError):
=======
    service = AiSuggestionService(client=DummyClient(DummyResponse({"suggestions": []})))
    with pytest.raises(AiSuggestionError):
>>>>>>> 7ad07fbb72f48a4bb9603622b9ff1ee8bc7dc865
        service.build_payload(title="", summary="", content="")

from typing import Any, List, Optional

from django.urls.resolvers import URLPattern

urlpatterns: Any

def staticfiles_urlpatterns(prefix: Optional[str] = ...) -> List[URLPattern]: ...

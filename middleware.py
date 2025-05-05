# middleware.py

from flask import Response, g, request, jsonify
from tenant_router import get_tenant_engine,get_tenant_mongo_db_engine
from sqlalchemy.orm import sessionmaker

def register_middleware(app):
    @app.before_request
    def before_request():
        try:
            # Step 1: Setup tenant DB session
            engine = get_tenant_engine()
            g.db = sessionmaker(bind=engine)()

            g.mongo_db = get_tenant_mongo_db_engine()

    #         # Step 2: Get user ID (use actual auth in production)
    #         user_id = g.get("user_id") or "user-002"
    #         if not user_id:
    #             return jsonify({"error": "Unauthorized"}), 401

    #         # Step 3: Fetch user's role
    #         user = g.db.query(User).filter_by(id=user_id).first()
    #         if not user or not user.role_id:
    #             return jsonify({"error": "User has no role assigned"}), 403

    #         # Step 4: Get role permissions
    #         permissions = (
    #             g.db.query(Permission)
    #             .join(RolePermission, Permission.id == RolePermission.permission_id)
    #             .filter(RolePermission.role_id == user.role_id)
    #             .all()
    #         )

    #         # Step 5: Match request path and method
    #         full_path = request.path
    #         base_path = "/api/"
    #         if full_path.startswith(base_path):
    #             parts = full_path.split('/')
    #             version_prefix = '/'.join(parts[:3])
    #             relative_path = full_path[len(version_prefix):] or "/"
    #         else:
    #             relative_path = full_path

    #         relative_path = relative_path.rstrip("/") or "/"
    #         req_method = request.method.upper()

    #         for perm in permissions:
    #             if perm.method == req_method and perm.path.rstrip("/") == relative_path:
    #                 return  # ✅ Permission granted

    #         return jsonify({"error": "Permission denied"}), 403

        except KeyError:
            return jsonify({"error": "Invalid tenant ID"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.teardown_request
    def teardown_request(exception=None):
        db_session = g.pop('db', None)
        if db_session:
            db_session.close()

    @app.after_request
    def add_security_headers(response: Response) -> Response:
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers.pop('X-Powered-By', None)
        return response

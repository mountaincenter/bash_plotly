# -*- coding: utf-8 -*-
from __future__ import annotations

from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.get("/health")
def health():
    return jsonify({"ok": True})

@health_bp.get("/ping")
def ping():
    return jsonify({"message": "flask connected"})

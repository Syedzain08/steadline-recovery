from flask import Flask, render_template, Response, url_for
from flask_frozen import Freezer
from shutil import copy


app = Flask(__name__)
freezer = Freezer(app)


# -- Home Route -- #
@app.route("/")
def index():
    return render_template("index.html")


# -- Services Routes -- #
@app.route("/services/motor-accidents/")
def motor_accidents():
    return render_template("services/motor_accidents.html")


@app.route("/services/vehicle-breakdown/")
def vehicle_breakdown():
    return render_template("services/vehicle_breakdown.html")


@app.route("/services/emergency-towing/")
def emergency_towing():
    return render_template("services/emergency_towing.html")


@app.route("/services/roadside-assistance/")
def roadside_assistance():
    return render_template("services/roadside_assistance.html")


@app.route("/services/vehicle-transport/")
def vehicle_transport():
    return render_template("services/vehicle_transport.html")


@app.route("/services/jumpstarts/")
def jumpstarts():
    return render_template("services/jumpstarts.html")


@app.route("/services/tyre-services/")
def tyre_services():
    return render_template("services/tyre_services.html")


@app.route("/services/scrap-vehicle-recovery/")
def scrap_vehicle_recovery():
    return render_template("services/scrap_vehicle_recovery.html")


# -- Privacy Policy Route -- #
@app.route("/privacy-policy/")
def privacy_policy():
    return render_template("privacy_policy.html")


# -- Robots Route -- #
@app.route("/robots.txt")
def robots_txt():
    lines = [
        "User-agent: *",
        "Disallow:",
        f"Sitemap: {url_for('sitemap', _external=True)}",
    ]
    return Response("\n".join(lines), mimetype="text/plain")


# --- Sitemap Route---- #
@app.route("/sitemap.xml")
def sitemap():
    urls = [
        {"loc": url_for("index", _external=True), "priority": "1.0"},
        {"loc": url_for("privacy_policy", _external=True), "priority": "0.5"},
        {"loc": url_for("motor_accidents", _external=True), "priority": "0.8"},
        {"loc": url_for("vehicle_breakdown", _external=True), "priority": "0.8"},
        {"loc": url_for("emergency_towing", _external=True), "priority": "0.8"},
        {"loc": url_for("roadside_assistance", _external=True), "priority": "0.8"},
        {"loc": url_for("vehicle_transport", _external=True), "priority": "0.8"},
        {"loc": url_for("jumpstarts", _external=True), "priority": "0.8"},
        {"loc": url_for("tyre_services", _external=True), "priority": "0.8"},
        {"loc": url_for("scrap_vehicle_recovery", _external=True), "priority": "0.8"},
    ]

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for url in urls:
        xml.append("  <url>")
        xml.append(f"    <loc>{url['loc']}</loc>")
        xml.append(f"    <priority>{url['priority']}</priority>")
        xml.append("  </url>")
    xml.append("</urlset>")

    return Response("\n".join(xml), mimetype="text/xml")


# -- Error Route -- #
@app.route("/404/")
def not_found():
    return render_template("404.html")


if __name__ == "__main__":
    app.config["FREEZER_BASE_URL"] = "https://steadline-recovery.vercel.app/"
    freezer.init_app(app)
    freezer.freeze()
    copy("build/404/index.html", "build/404.html")

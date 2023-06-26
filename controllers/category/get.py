from flask import render_template


def category_get_controller(category, request):
    return render_template("category.html", category=category)

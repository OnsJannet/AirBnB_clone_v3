#!/usr/bin/python3
""" Task 12 : Reviews  """
from flask import request, jsonify, abort
from api.v1.views import app_views
from models import storage, place, review, user


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """ Return all reviews linked to a place """
    s_place = storage.get(place.Place, place_id)
    if s_place is None:
        abort(404)
    print(s_place)
    reviews = [c.to_dict() for c in s_place.reviews]
    return (jsonify(reviews), 200)


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """ Delete a review  """
    reviews = storage.all(review.Review).values()
    for one_review in reviews:
        if one_review.id == review_id:
            storage.delete(one_review)
            storage.save()
            return(jsonify({}))
    abort(404)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """  get review  """
    reviews = storage.all(review.Review).values()
    list_reviews = [c.to_dict() for c in reviews]
    for one_review in list_reviews:
        if one_review['id'] == review_id:
            return (jsonify(one_review))
    abort(404)

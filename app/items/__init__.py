from typing import List
from fastapi import APIRouter

from .schema import ItemListModel, ItemDetailModel

from .handlers.create import create_item
from .handlers.read import list_items, get_item
from .handlers.update import update_item
from .handlers.delete import delete_item

router = APIRouter()

# TODO: Exception handling

# GET
router.add_api_route("/", endpoint=list_items, response_model=List[ItemListModel])
router.add_api_route("/{item_id}", endpoint=get_item, response_model=ItemDetailModel)

# POST
router.add_api_route(
    "/",
    methods=["POST"],
    endpoint=create_item,
    response_model=ItemDetailModel,
    status_code=201
)

# PUT
router.add_api_route(
    "/{item_id}",
    methods=["PUT"],
    endpoint=update_item,
    response_model=ItemDetailModel,
    status_code=200
)

# DELETE
router.add_api_route(
    "/{id}",
    methods=["DELETE"],
    endpoint=delete_item,
    status_code=204
)

# router.add_api_route("/me", endpoint=auth_info, response_model=AccountDetailModel)
# router.add_api_route("/{id}", endpoint=get_merchant, response_model=AccountDetailModel)
#
# router.add_api_route("/{id}/feeds", endpoint=list_merchant_feeds, response_model=List[FeedListModel])
# router.add_api_route("/{id}/feeds/{feed_id}", endpoint=get_merchant_feed, response_model=FeedDetailModel)
#

#
# # PUT
# router.add_api_route(
#     "/{id}",
#     methods=["PUT"],
#     endpoint=update_merchant,
#     response_model=AccountDetailModel
# )
# router.add_api_route(
#     "/{id}/feeds/{feed_id}",
#     methods=["PUT"],
#     endpoint=update_merchant_feed,
#     response_model=FeedDetailModel
# )
# router.add_api_route(
#     "/{id}/feeds/{feed_id}/trigger",
#     methods=["PUT"],
#     endpoint=trigger_merchant_feed
# )
#

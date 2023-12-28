3 model classes is defined in this program. first is product model with one field. second named productitem is for adding product items and its quantity. and the last one named producttransition is to specify import/export product items and updating their quantity(when we export an item its quantity lessen once and vise versa)
it is needed to say that its assumed we dont have permission to add duplicated product to productitem class.if it happen, the quantity of the existed product item id added once.
some exceptions are noted in serializer class:
if the quantity of a product item is zero for transition or want to add an item that is not existed in products, we will get validation error.

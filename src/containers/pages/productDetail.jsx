import Layout from "../../hocs/Layout";
import {useParams} from 'react-router'
import { connect } from 'react-redux';
import {get_product, get_related_products } from "../../redux/actions/products";
import { useEffect, useState } from "react";
import ImageGallery from "../../components/product/ImageGallery";
import { useNavigate } from "react-router";
import { 
  get_items,
  add_item,
  get_total,
  get_item_total
} from '../../redux/actions/cart'

import { Disclosure, RadioGroup, Tab } from '@headlessui/react'
// import { StarIcon } from '@heroicons/react/solid'
// import { HeartIcon, MinusSmIcon, PlusSmIcon } from '@heroicons/react/outline'



const ProductDetail = ({get_product, get_related_products, product, get_items, get_item_total, add_item, get_total}) => {

  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const addToCart = async () => {
    if (product && product !== null && product !== undefined && product.quantity > 0) {
        setLoading(true)
        await add_item(product);
        await get_items();
        await get_total();
        await get_item_total();
        setLoading(false)
        navigate('/cart')
    }
  }

    const params = useParams()
    const productId = params.productId
    // const [selectedColor, setSelectedColor] = useState(product.colors[0])


    useEffect(() => {
      window.scrollTo(0,0)
        get_product(productId)
        get_related_products(productId)
    }, [get_product, get_related_products, productId])


    return (
        <Layout>
             <div className="bg-white">
      <div className="max-w-2xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
        <div className="lg:grid lg:grid-cols-2 lg:gap-x-8 lg:items-start">
        
        <ImageGallery photo={product && product.photo} />
          {/* Product info */}
          <div className="mt-10 px-4 sm:px-0 sm:mt-16 lg:mt-0">
            <h1 className="text-3xl font-extrabold tracking-tight text-gray-900">{product && product.name}</h1>

            <div className="mt-3">
              <h2 className="sr-only">Product information</h2>
              <p className="text-3xl text-gray-900">{product && product.price}</p>
            </div>

            <div className="mt-6">
              <h3 className="sr-only">Description</h3>

              <div
                className="text-base text-gray-700 space-y-6"
                dangerouslySetInnerHTML={{ __html: product && product.description }}
              />
            </div>


            <div className="mt-6">
              <div className="mt-10 flex sm:flex-col1">

              <p className="mt-4">
                  {
                      product && 
                      product !== null &&
                      product !== undefined && 
                      product.quantity > 0 ? (
                          <span className='text-green-500'>
                              In Stock
                          </span>
                      ) : (
                          <span className='text-red-500'>
                              Out of Stock
                          </span>
                      )
                  }
              </p>
              {/* ADD TO CART BUTTON AND FUNCTION */}
              <div className="mt-4 flex sm:flex-col1">
                {loading?<button 
                  className="max-w-xs flex-1 bg-indigo-600 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-50 focus:ring-indigo-500 sm:w-full">
                </button>:
                <button 
                onClick={addToCart}
                className="max-w-xs flex-1 bg-indigo-600 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-50 focus:ring-indigo-500 sm:w-full">
                  Agregar al Carrito
              </button>}
              {/* ADD TO WISH LIST ICON AND FUNCTION */}
                <button
                  className="ml-4 py-3 px-3 rounded-md flex items-center justify-center text-gray-400 hover:bg-gray-100 hover:text-gray-500"
                >
                  {/* HEART ICON */}
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-6 h-6">
                    <path d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                    </svg>
                  <span className="sr-only">Add to favorites</span>
                </button>
              </div>
            </div>
            <section aria-labelledby="details-heading" className="mt-12">
              <h2 id="details-heading" className="sr-only">
                Additional details
              </h2>
              {/* AGREGAR LA SECCION DE MAS INFORMACION DESPUES */}
            </section>
          </div>
        </div>
      </div>
    </div>
  </div>
        </Layout>
    )
}
const mapStateToProps = state => ({
    product: state.Products.product,
    // isAuthenticated: state.Auth.isAuthenticated,
    // wishlist: state.Wishlist.wishlist,
    // review: state.Reviews.review,
    // reviews: state.Reviews.reviews
})


export default connect(mapStateToProps, {
    get_product,
    get_related_products,
    get_items,
    add_item,
    get_total,
    get_item_total,
    // add_wishlist_item, 
    // get_wishlist_items, 
    // get_wishlist_item_total,
    // remove_wishlist_item,
    // get_reviews,
    // get_review,
    // create_review,
    // update_review,
    // delete_review,
    // filter_reviews
}) (ProductDetail)
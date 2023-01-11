
import { useState, useEffect} from "react"
import { Carousel } from 'react-responsive-carousel';
import { render } from "react-dom";
import Slider from "react-slick";
import { Link } from "react-router-dom";
import  YouTube  from 'react-youtube';
import './Banner.css';
import React from 'react';
// import video from './../../video.mp4'
/* This example requires Tailwind CSS v2.0+ */
export default function Banner() {
  const [currentWallpaper, setCurrentWallpaper] = useState(0)
  const divStyle = {
    backgroundImage: "url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/9757d496-239b-46c5-baea-6873cbfe9b3d/ddmuwp6-6d439b6d-567a-40a2-988e-6cb42e743be8.jpg')"
  };





  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000
  };

  const frameStyle = {
    width: '44',
    height: '64',
    borderRadius: '50%',
    overflow: 'hidden'
  };
  const imageStyle = {
    width: '10%',
    height: '10%',
    objectFit: 'cover',
    objectPosition: 'center'
  };



  const options = {
    playerVars: {
      autoplay: 1, // start the video automatically
      controls: 0, // hide the default player controls
      modestbranding: 1, // hide the YouTube logo
      showinfo: 0 // hide the video title and uploader
    }
  };

  const opts = {
    height: '1080',
    width: '720',
    playerVars: {
      // https://developers.google.com/youtube/player_parameters
      autoplay: 1,
    },
  };

    return (
      <div className="relative bg-white overflow-hidden"
      >
        {/* <YouTube videoId="7H7cTSml5zk"  opts={opts} style={{width: 1000, height:1000}}/> */}
        {/* <video src={video} autoPlay loop muted style={{width: 1900, opacity: 8}}></video> */}

        <div className="pt-16 pb-80 sm:pt-24 sm:pb-40 lg:pt-40 lg:pb-48" style={{ marginTop: -700, opacity: 1}}>
          <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 sm:static"
          >
            <div className="sm:max-w-lg" 
            style={{opacity: 1}}
            >
              <h1 className="text-4xl font font-extrabold tracking-tight text-gray-900 sm:text-6xl" style={{opacity:1, marginTop:-300}}>
                Find your Art Oasis in this World
              </h1>
             
              {/* <p className="mt-4 text-xl text-gray-500">
                Hello My Name is Nathalie and this is my personal Art Oasis where you can see and if you want buy my art
              </p> */}
            </div>
            <div>
              <div className="mt-10">
                {/* Decorative image grid */}
                <div
                  aria-hidden="true"
                  className="pointer-events-none lg:absolute lg:inset-y-0 lg:max-w-7xl lg:mx-auto lg:w-full"
                >
                  {/* <div className="absolute transform sm:left-1/2 sm:top-0 sm:translate-x-8 lg:left-1/2 lg:top-1/2 lg:-translate-y-1/2 lg:translate-x-8">
                    <div className="flex items-center space-x-6 lg:space-x-8">
                      <div className="flex-shrink-0 grid grid-cols-1 gap-y-6 lg:gap-y-8">
                        <div style={frameStyle}>
                          <img
                            src="media\photos\2022\12\1672003075215.jpg"
                            alt=""
                            style={imageStyle}
                          />
                        </div>
                        <div className="w-44 h-64 rounded-lg overflow-hidden">
                          <img
                            src= "media\photos\2022\12\dfb9ij1-a8237fe4-2555-4744-b2ce-676f608637c5.jpg"
                            alt=""
                            className="w-full h-full object-center object-cover"
                          />
                        </div>
                      </div>
                      <div className="flex-shrink-0 grid grid-cols-1 gap-y-6 lg:gap-y-8">
                        <div className="w-44 h-64 rounded-lg overflow-hidden">
                          <img
                            src="media\photos\2022\12\1672003075296.jpg"
                            alt=""
                            className="w-full h-full object-center object-cover max-w-full max-h-full"
                          />
                        </div>
                        <div className="w-44 h-64 rounded-lg overflow-hidden">
                          <img
                            src="media\photos\2022\12\1672003075538.jpg"
                            alt=""
                            className="w-full h-full object-center object-cover max-w-full max-h-full"
                          />
                        </div>
                        <div className="w-44 h-64 rounded-lg overflow-hidden">
                          <img
                            src="media\photos\2022\12\1672003075277.jpg"
                            alt=""
                            className="w-full h-full object-center object-cover max-w-full max-h-full"
                          />
                        </div>
                      </div>
                      <div className="flex-shrink-0 grid grid-cols-1 gap-y-6 lg:gap-y-8">
                        <div className="w-44 h-64 rounded-lg overflow-hidden">
                          <img
                            src="media\photos\2022\12\dfb9ij1-a8237fe4-2555-4744-b2ce-676f608637c5.jpg"
                            alt=""
                            className="w-full h-full object-center object-cover max-w-full max-h-full"
                          />
                        </div>
                        <div className="w-44 h-64 rounded-lg overflow-hidden">
                          <img
                            src="media\photos\2022\12\1672003075256.jpg"
                            alt=""
                            className="w-full h-full object-center object-cover max-w-full max-h-full"
                          />
                        </div>
                      </div>
                    </div>
                  </div> */}
                </div>
               
                <a
                  href="/shop"
                  className="inline-block text-center bg-yellow-600 border border-transparent rounded-md py-3 px-8 font-medium text-white hover:bg-indigo-700"
                >
                  Entdecken
                </a>
              
              </div>
            </div>
          </div>
        </div>
      
      </div>
    )
  }

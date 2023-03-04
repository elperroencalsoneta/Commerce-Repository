import React, { useEffect, useState, useRef } from "react";
import { GoogleMap, useJsApiLoader,   Marker} from '@react-google-maps/api';
import { Wrapper, Status, Map } from "@googlemaps/react-wrapper";



export default function Banner() {
     // GET USER'S LOCATION
     const [userCoords, setUserCoords] = useState(null);
  
     const [stores, setStores] = useState(null);
     const ref = useRef(null);
     const [map, setMap] = useState();


     
     const render = (Status) => {
      return <h1>{Status}</h1>;
    };

    //  bringing the map

    useEffect(() => {
      if (ref.current && !map) {
        setMap(new window.google.maps.Map(ref.current, {}));
      }
    }, [ref, map]);

   
  
    useEffect(() => {
      navigator.geolocation.getCurrentPosition(position => {
          setUserCoords({
            latitude: position.coords.latitude,
            longitude: position.coords.longitude
          });
        });
  }, [])

  useEffect(() => {
      if (userCoords){
          fetch('http://localhost:8000/api/supermarket/store_locator', {
      method: 'POST',
      body: JSON.stringify(userCoords),
      headers: {
          'Content-Type': 'application/json'
      },
  }).then(response => response.json())
    .then(data => {
     //  setStores(data.stores);
      console.log(data)
      setStores(data.stores)
    });
      }
  }, [userCoords])


 

    return (
      <div className="relative bg-white overflow-hidden">
        <div className="pt-16 pb-80 sm:pt-24 sm:pb-40 lg:pt-40 lg:pb-48">
          <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 sm:static">
            <div className="sm:max-w-lg">
              <h1 className="text-4xl font font-extrabold tracking-tight text-gray-900 sm:text-6xl">
                Find the product close of you
              </h1>
              <p className="mt-4 text-xl text-gray-500">
                This year, our new summer collection will shelter you from the harsh elements of a world that doesn't care
                if you live or die.
              </p>
            </div>
            <div>
            <div className="flex flex-wrap -mx-4">
                {stores && stores.map(store => (
                  <div key={store.pk} className="w-1/3 px-4 mb-4">
                    <div className="max-w-sm rounded overflow-hidden shadow-lg bg-white">
                      <img src={store.fields.photo} alt={store.fields.name} className="w-full" />
                      <div className="px-6 py-4">
                        <div className="font-bold text-xl mb-2">{store.fields.name}</div>
                        <p className="text-gray-700 text-base">{store.fields.address}</p>
                        <p className="text-gray-700 text-base">{store.fields.distance} km</p>
                      </div>
                      <div className="px-6 py-4">
                        <a href={store.fields.website} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:text-blue-800">Visit website</a>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
              {/* <div className="mt-10"> */}
                {/* Decorative image grid */}

                <div className="flex">
               
              
                  
                  {/* HERE GOES THE MAP */}
                  {/* ADD LATER WHEN MONEY FOR API */}
                  <Wrapper apiKey={"AIzaSyDT_uSH8OsDau8YoFTgXSiOLzhVt1NqNp8"} render={render}>
                   <div  ref={ref}/>
                  </Wrapper>
                </div>
                <a
                  href="#"
                  className="inline-block text-center bg-indigo-600 border border-transparent rounded-md py-3 px-8 font-medium text-white hover:bg-indigo-700"
                >
                  Shop Collection
                </a>
              {/* </div> */}
            </div>
          </div>
        </div>
      </div>
    )
  }
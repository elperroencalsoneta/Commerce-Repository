import {Provider} from 'react-redux';
import store from './store'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import Home from './containers/pages/Home';
import Error404 from './containers/errors/Error404';

import Activate from './containers/auth/Activate';
import Signup from './containers/auth/Signup';
import Login from './containers/auth/Login';
import ResetPassword from './containers/auth/Reset_Password';
import ResetPasswordConfirm from './containers/auth/Reset_Password_Confirm';
import Shop from './containers/pages/Shop';
import ProductDetail from './containers/pages/productDetail';
import Search from './containers/pages/Search';
import Cart from './containers/pages/Cart';
import Checkout from './containers/pages/Checkout';
import ThankYou from './containers/pages/ThankYou';
import Dashboard from './containers/pages/Dashboard';
import OfferList from './containers/pages/Offers';
// import PrivateRoute from  './hocs/PrivateRoute'

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          <Route path="*" element={<Error404/>} />
          <Route exact path="/" element={<Home/>} />
          <Route exact path='/cart' element={<Cart/>}/>
          <Route exact path='/checkout' element={<Checkout/>}/>
          
          <Route exact path="/signup" element={<Signup/>} />
          <Route exact path="/login" element={<Login />} />
          <Route exact path="/activate/:uid/:token" element={<Activate/>} />
          <Route exact path="/reset_password" element={<ResetPassword/>} />
          <Route exact path='/password/reset/confirm/:uid/:token' element={<ResetPasswordConfirm/>} />
       
          <Route exact path='/thankyou' element={<ThankYou/>}/>

          <Route exact path='/shop' element={<Shop/>}/>
          <Route exact path='/product/:productId' element={<ProductDetail/>}/>
          <Route exact path='/search' element={<Search/>}/>
          <Route exact path='/offers' element={<OfferList/>} />
         
          <Route exact path='/dashboard' element={<Dashboard/>}/>
        </Routes>
      </Router>
    </Provider>
    
  );
}

export default App;

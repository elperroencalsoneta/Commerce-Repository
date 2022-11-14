import { connect } from "react-redux";
import { Route, Navigate } from "react-router-dom";

const PrivateRoute = ({
    celement: Element,
    auth: {
        isAuthenticated, loading
    }, ...rest
}) => (
    <Route
        {...rest}
        render={props => !isAuthenticated && !loading ? (
            <Navigate to='/login' />
        ): (
            <Element {...props} />
        )}
    />
);

const mapStateToProps = state => ({
    auth: state.Auth
})

export default PrivateRoute;
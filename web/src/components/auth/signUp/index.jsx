import React from "react";
import StorageUtil from "../../../service/helper/storage";
import { useLocation, Navigate, useNavigate } from "react-router-dom";
import { SignUpForm } from "./form";
import RequestUtil from "../../../service/helper/requestUtil";
import { urlMap } from "../../../service/urls";
import { useSnackbar } from "notistack";

export const SignUp = () => {
  const location = useLocation();
  const navigate = useNavigate();
  
  const { enqueueSnackbar } = useSnackbar();
  const isAuthenticated = StorageUtil.getToken("token");
  if (isAuthenticated && location.pathname === "/register") {
    return <Navigate to="/" />;
  }
  const { prefix, endpoints } = urlMap.auth;
  const handleLogin = (data) => {
    console.log(data)
    RequestUtil.apiCallWithRefreshToken(prefix + endpoints.register, data, "POST")
      .then((req) => {
        navigate("/register/verify-email");
      })
      .catch((error) => enqueueSnackbar(error, "error"));
  };

  return (
    <>
      <SignUpForm handleLogin={handleLogin} />
    </>
  );
};

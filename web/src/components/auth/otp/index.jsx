import React from "react";
import StorageUtil from "../../../service/helper/storage";
import { useLocation, Navigate, useNavigate } from "react-router-dom";
import { OtpForm } from "./form";
import RequestUtil from "../../../service/helper/requestUtil";
import { urlMap } from "../../../service/urls";
import { useSnackbar } from "notistack";

export const Otp = () => {
  const location = useLocation();
  const navigate = useNavigate();
  
  const { enqueueSnackbar } = useSnackbar();
  const isAuthenticated = StorageUtil.getToken("token");
  if (isAuthenticated && location.pathname === "/register") {
    return <Navigate to="/" />;
  }
  const { prefix, endpoints } = urlMap.auth;
  const handleLogin = (data) => {
    RequestUtil.apiCallWithRefreshToken(prefix + endpoints.verifyEmail, data, "POST")
      .then((req) => {
        navigate("/login");
        enqueueSnackbar("Register successfully !");
      })
      .catch((error) => enqueueSnackbar(error, "error"));
  };

  return (
    <>
      <OtpForm handleLogin={handleLogin} />
    </>
  );
};

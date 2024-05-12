import * as React from "react";
import { Outlet, Navigate } from "react-router-dom";
import StorageUtil from "../../../service/helper/storage";

export default function PrivateRoute() {
  const isAuthenticated = StorageUtil.getToken();
  return isAuthenticated ? <Outlet /> : <Navigate to="/" />;
}

PrivateRoute.displayName = "PrivateRoute";

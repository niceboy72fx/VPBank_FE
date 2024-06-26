import React from "react";
import AccountCircle from "@mui/icons-material/AccountCircle";
import MenuItem from "@mui/material/MenuItem";
import Badge from "@mui/material/Badge";
import IconButton from "@mui/material/IconButton";
import NotificationsIcon from "@mui/icons-material/Notifications";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import Tooltip from "@mui/material/Tooltip";
import Box from "@mui/material/Box";
import StorageUtil from "../../../../service/helper/storage";
import NavUtil from "../../../../service/helper/navUtil";
import { useNavigate } from "react-router-dom";


export const ToolBarCustom = () => {
  const [anchorElUser, setAnchorElUser] = React.useState(null);
  const username = StorageUtil.getStorageObj("username");
  const navigate = useNavigate();

  const settings = ["Profile", "Logout"];
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const handleItemMenu = (event) => {
    if (event.target.textContent === "Logout") {
      NavUtil.logout();
    }
  };

  return (
    <div className="flex items-center justify-center">
      <IconButton color="inherit">
        <Badge badgeContent={4} color="warning">
          <NotificationsIcon color="inherit" />
        </Badge>
      </IconButton>
      <Box sx={{ marginLeft: 7 }}>
        <Tooltip title="Open settings">
          <IconButton
            onClick={handleOpenUserMenu}
            sx={{ display: "flex", justifyContent: "center" }}
          >
            <AccountCircle sx={{ color: "white", width: 32, height: 32 }} />
            <p className="font-bold text-white text-sm p-3 ">{username}</p>
          </IconButton>
        </Tooltip>
        <Menu
          sx={{ mt: "45px" }}
          id="menu-appbar"
          anchorEl={anchorElUser}
          anchorOrigin={{
            vertical: "top",
            horizontal: "right",
          }}
          keepMounted
          transformOrigin={{
            vertical: "top",
            horizontal: "right",
          }}
          open={Boolean(anchorElUser)}
          onClose={handleCloseUserMenu}
        >
          {settings.map((setting) => (
            <MenuItem key={setting} onClick={handleCloseUserMenu}>
              <Typography onClick={handleItemMenu} textAlign="center">
                {setting}
              </Typography>
            </MenuItem>
          ))}
        </Menu>
      </Box>
    </div>
  );
};

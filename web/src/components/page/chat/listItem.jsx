import * as React from "react";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import DashboardIcon from "@mui/icons-material/Dashboard";
import Avatar from "@mui/material/Avatar";

export const ListUser = () => {
  return (
    <React.Fragment>
      <ListItemButton>
        <ListItemIcon>
          <div className="flex items-center flex-row ">
            <Avatar sx={{ width: 32, height: 32, fontSize: 15 }}>U</Avatar>
          </div>
        </ListItemIcon>
        <ListItemText primary="User 1" />
      </ListItemButton>
    </React.Fragment>
  );
};

// export const secondaryListItems = (
//   <React.Fragment>
//     <ListItemButton>
//       <ListItemIcon>
//         <AssignmentIcon />
//       </ListItemIcon>
//       <ListItemText primary="Current month" />
//     </ListItemButton>
//   </React.Fragment>
// );

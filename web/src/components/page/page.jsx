import DashBoard from "./dashBoard";
import Doctor from "./doctor";
import Medicine from "./medicine";
import AssignmentIcon from "@mui/icons-material/Assignment";
import Test from "./test";
import Chat from "./chat";
import HealthRecord from "./healthRecord";

export const pageCms = [
  {
    path: "/chat",
    element: <Chat />,
    name: "Chat",
    children: [
      {
        icon: <AssignmentIcon />,
        path: "",
        element: <Test />,
        name: "Chat",
      },
    ],
  },
];

import React from "react";
import SendIcon from "@mui/icons-material/Send";
import Button from "@mui/material/Button";
import OutlinedInput from "@mui/material/OutlinedInput";
import Avatar from "@mui/material/Avatar";
import FilePresentIcon from "@mui/icons-material/FilePresent";
import ImageIcon from "@mui/icons-material/Image";
import SentimentVerySatisfiedIcon from "@mui/icons-material/SentimentVerySatisfied";
import Divider from "@mui/material/Divider";

const ChatContent = () => {
  return (
    <div className="my-16 h-[700px] w-full absolute bottom-0 overflow-y-auto">
      <div>
        <Divider />
        <div className="m-5">
          <div className="flex items-center flex-row ">
            <Avatar sx={{ width: 32, height: 32, fontSize: 15 }}>U</Avatar>
            <p className="m-2 font-bold ">User 1</p>
          </div>
          <p className="py-4">
            If you want to position the element relative to its parent
            container, you should make sure the parent container has a position
            property set to relative, absolute, fixed, or sticky. Here's an
            example:
          </p>
        </div>
      </div>
      <div>
        <Divider />
        <div className="m-5">
          <div className="flex items-center flex-row ">
            <Avatar sx={{ width: 32, height: 32, fontSize: 15 }}>U</Avatar>
            <p className="m-2 font-bold ">User 1</p>
          </div>
          <p className="py-4">
            If you want to position the element relative to its parent
            container, you should make sure the parent container has a position
            property set to relative, absolute, fixed, or sticky. Here's an
            example:
          </p>
        </div>
      </div>
    </div>
  );
};

const Room = () => {
  return (
    <div className="relative h-full">
      <div className="w-full bg-white p-3 flex items-center shadow-2xl absolute top-0 z-50">
        <Avatar>U</Avatar>
        <p className="m-2 font-bold">User 1</p>
      </div>
      <ChatContent />
      <div className="w-full bg-white p-3 flex items-center shadow-2xl absolute bottom-0">
        <Button variant="outlined" color="inherit" sx={{ margin: "10px" }}>
          <FilePresentIcon fontSize="medium" />
        </Button>
        <Button variant="outlined" color="inherit" sx={{ margin: "10px" }}>
          <ImageIcon fontSize="medium" />
        </Button>
        <Button variant="outlined" color="inherit" sx={{ margin: "10px" }}>
          <SentimentVerySatisfiedIcon fontSize="medium" />
        </Button>
        <OutlinedInput
          size="small"
          placeholder="Enter message"
          sx={{ width: "100%" }}
        />
        <Button variant="outlined" color="inherit" sx={{ margin: "10px" }}>
          <SendIcon fontSize="medium" />
        </Button>
      </div>
    </div>
  );
};

export default Room;

import axios from "axios";

export default class Util {
  static responseInterceptor() {
    axios.defaults.withCredentials = false;
    axios.defaults.xsrfHeaderName = "X-CSRFToken";
    axios.defaults.xsrfCookieName = "csrftoken";
  }

  static getValueFromEvent(e) {
    const { target } = e;
    return target.value || "";
  }

//   static isoToReadableDatetimeStr(strDate) {
//     if (!strDate) {
//       return strDate;
//     }
//     if (!strDate.includes("T")) {
//       return strDate;
//     }
//     const dateArr = strDate.split("T");
//     let datePart = dateArr[0];
//     let timePart = dateArr[1];
//     try {
//       datePart = datePart.split("-").reverse().join("/");
//       timePart = timePart.split(":");
//       timePart.pop();
//       timePart = timePart.join(":");
//       return datePart + " " + timePart;
//     } catch (_err) {
//       return strDate;
//     }
//   }
}

import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

import {
    get,
    getDatabase,
    onValue,
    push,
    ref,
    remove,
    set
} from "firebase/database";

const firebaseConfig = {
  apiKey: "AIzaSyC3YjZX88pVOD8KffDGZxhryPP2loJlBt4",
  authDomain: "trip-planner-358c2.firebaseapp.com",
  projectId: "trip-planner-358c2",
  storageBucket: "trip-planner-358c2.appspot.com",
  messagingSenderId: "622372293232",
  appId: "1:622372293232:web:93253cfd1b3159ffbe02b5",
  measurementId: "G-HJK7Q36VEX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export const db = getDatabase(app);

function randomID() {
    return Math.random().toString(36).substring(2);
}

export const addTrip = async (title, dateStart, dateEnd) => {
    //let actualTimeStart = new Date(timeStart).getTime() / 1000;
    //let actualTimeEnd = new Date(timeEnd).getTime() / 1000;
    
    return set(ref(db, `/trip/${randomID()}`), {
        title: title,
        startDate: dateStart,
        endDate: dateEnd,
    })
}

export const addEvent = async (id, title, description) => {
    //let actualTimeStart = new Date(timeStart).getTime() / 1000;
    //let actualTimeEnd = new Date(timeEnd).getTime() / 1000;
    
    return set(ref(db, `/trip/${randomID()}`), {
        title: title,
        startDate: actualTimeStart,
        endDate: actualTimeEnd,
    })
}
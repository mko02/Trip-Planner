import React from 'react'
import { ReactCalendar } from "../Components/Calendar/ReactCalendar.js"

function Home() {
  return (
    <><div>Home</div><div>
      <ReactCalendar 
        //Dates to be highlighted
        tripDate = {[
          'Jul 15 2022',
          'Jul 16 2022',
          'Jul 20 2022']
        }
      />
    </div></>
  )
}

export default Home
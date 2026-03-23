import React, { useEffect, useState } from 'react'
import axios from "axios"
import Loader from './Loader'
// import Loader from '../'
function Waether({ lat },) {
    console.log(lat.lat)
    console.log(lat.lng)
    const [weatherLdin, setweatherldinghg] = useState(false)

    useEffect(() => {
        const getWaether = async () => {
            const key = import.meta.env.VITE_WEATHER_API_KEY
         
            try {
                setweatherldinghg(true)
                const data = await axios.get(`https://api.openweathermap.org/data/2.5/weather?lat=${lat.lat.toFixed(6)}&lon=${lat.lng.toFixed(6)}&appid=${key}&units=metric`)
                console.log(data, "data")
                setweatherldinghg(false)
            } catch (error) {
                console.log("err ferom waether")

            }
        }
        getWaether()
    }, [])

    return (
        <>

            {weatherLdin && <Loader loadername="Fetching real-time weather..." />}
        </>
    )
}

export default Waether
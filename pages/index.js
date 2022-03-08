import React, { useState, useEffect } from 'react'
import Head from 'next/head'
import Navbar from '../components/Navbar'
import DropdownMenu from '../components/DropdownMenu';
import Hero from '../components/Hero';
import Country from '../components/Country';
import Contact from '../components/Contact';
import Footer from '../components/Footer';
import HomeAmerica from './America';


export const getStaticProps = async () => {
  const res = await fetch('http://127.0.0.1:8000/America')
  const data = await res.json();

  return {
    props: { america: data }
  }
}

export default function Home({ america }) {

  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen);
  }


  return (
    <div >
      <Head>
        <title>Real Estate || Home</title>
      </Head>

      <Navbar toggle={toggle} />
      <DropdownMenu isOpen={isOpen} toggle={toggle} />

      <Hero />

      <div className='h-[14rem] w-full font-bold pt-[6rem] text-center'>
        <h1 className='w-[21.6rem] text-xl p-auto h-auto m-auto sm:text-2xl lg:text-3xl lg:w-[28rem]'>We are available in many
        well-known countries</h1>
      </div>
      <Country />
      
      <div className='h-[14rem] w-full font-bold pt-[6rem] text-center  '>
        <h1 className='w-[21.6rem] mx-auto text-xl sm:text-2xl lg:text-3xl lg:w-[28rem]'>Recently Added</h1>
      </div>
      <HomeAmerica america={america} />
      
      {/* Footer */}
      <Footer />

    </div>
  )
}

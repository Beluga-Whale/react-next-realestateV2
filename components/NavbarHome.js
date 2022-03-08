import React, { useState, useEffect } from 'react'
import Image from 'next/image'
import Link from 'next/link'


const NavbarHome = ({ toggle }) => {

    const toggleHome = () => {
        scroll.scrollToTop()
    }


    return (
        <div>
            <nav className='nav-change-home'>
                <div className="">
                    <Link href="/" onClick={toggleHome} className="hover:animate-bounce cursor-pointer">
                        <a >
                            <Image src={'/Logo.svg'} alt="Logo" width={130} height={35} />
                        </a>
                    </Link>
                </div>
                <div className='text-white cursor-pointer md:hidden' onClick={toggle}>
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" /></svg>
                </div>
                <div className="text-white md:block hidden ">
                    <div className='flex  justify-between w-96 xl:w-30'>
                        <Link href="/" onClick={toggleHome} className="">
                            <a className="nav-animate" href="">HOME</a>
                        </Link>

                        <Link href="/" className="nav-animate">
                            <a className="nav-animate" href="">COUNTRIES</a>
                        </Link>

                        <Link href="/" className="nav-animate">
                            <a className="nav-animate" href="">REAL ESTATE</a>
                        </Link>

                        <Link href="/" className="nav-animate">
                            <a className="nav-animate" href="">CONTACT</a>
                        </Link>
                    </div>
                </div>
            </nav>
        </div>
    )
}

export default NavbarHome
import React, { useState, useEffect } from 'react'
import Image from 'next/image'
import { Link as LinkS, animateScroll as scroll } from 'react-scroll'

const Navbar = ({ toggle }) => {

    const [color, setColor] = useState(false)

    const changeColor = () => {
        if (window.scrollY >= 80) {
            setColor(true)
        } else {
            setColor(false)
        }
    }

    useEffect(() => {
        window.addEventListener('scroll', changeColor)
    }, [])

    const toggleHome = () => {
        scroll.scrollToTop()
    }


    return (
        <div>
            <nav className={color ? 'nav-change' : 'nav-container'}>
                <div className="">
                    <LinkS to="/"
                        onClick={toggleHome} 
                        className="hover:animate-bounce cursor-pointer"
                        smooth={true}
                        duration={300}
                        spy={true}
                        exact='true'
                        offset={-220}
                    >
                        <Image src={'/Logo.svg'} alt="Logo" width={130} height={35} />
                    </LinkS>
                </div>
                <div className='text-white cursor-pointer md:hidden' onClick={toggle}>
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" /></svg>
                </div>
                <div className="text-white md:block hidden ">
                    <div className='flex justify-between w-96 xl:w-30'>
                        <LinkS  to="/" onClick={toggleHome} className="nav-animate "
                            smooth={true}
                            duration={300}
                            spy={true}
                            exact='true'
                            offset={-220}
                        >
                            HOME
                        </LinkS>

                        <LinkS to="country" className="nav-animate"
                            smooth={true}
                            duration={300}
                            spy={true}
                            exact='true'
                            offset={-220}
                        >
                            COUNTRIES
                        </LinkS>

                        <LinkS to="america" className="nav-animate"
                            smooth={true}
                            duration={300}
                            spy={true}
                            exact='true'
                            offset={-220}
                        >
                            REAL ESTATE
                        </LinkS>

                        <LinkS to="footer" className="nav-animate"
                            smooth={true}
                            duration={300}
                            spy={true}
                            exact='true'
                            offset={-220}
                        >
                            CONTACT
                        </LinkS>
                    </div>
                </div>
            </nav>
        </div>
    )
}

export default Navbar
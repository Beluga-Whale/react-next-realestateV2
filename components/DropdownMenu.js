import React from 'react'
import { Link as LinkS, animateScroll as scroll } from 'react-scroll'

const DropdownMenu = ({ isOpen, toggle }) => {
    return (
        <div >
            <div className={isOpen ? 'drop-open' : 'hidden'} onClick={toggle}>

                <div className="text-white cursor-pointer absolute top-5 right-10 hover:text-[#FFAC12] " onClick={toggle}>

                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /></svg>

                </div>

                <div className='flex pt-8 flex-col justify-around h-1/2 cursor-pointer'>
                    <LinkS onClick={toggle} to="hero-fade" ><a className="drop-items"> HOME </a></LinkS>
                    <LinkS onClick={toggle} to="country" ><a className="drop-items"> COUNTRIES </a></LinkS>
                    <LinkS onClick={toggle} to="america" ><a className="drop-items"> REAL ESTATE </a></LinkS>
                    <LinkS onClick={toggle} to="footer" ><a className="drop-items"> CONTACT </a></LinkS>
                </div>

            </div>
        </div>
    )
}

export default DropdownMenu
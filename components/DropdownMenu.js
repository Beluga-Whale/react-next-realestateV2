import React from 'react'
import Link from 'next/link'

const DropdownMenu = ({ isOpen, toggle }) => {
    return (
        <div >
            <div className={isOpen ? 'drop-open' : 'hidden'} onClick={toggle}>

                <div className="text-white cursor-pointer absolute top-5 right-10 hover:text-[#FFAC12] " onClick={toggle}>

                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /></svg>

                </div>

                <div className='flex pt-8 flex-col justify-around h-1/2 cursor-pointer'>
                    <Link href="/" ><a className="drop-items"> HOME </a></Link>
                    <Link href="/" ><a className="drop-items"> COUNTRIES </a></Link>
                    <Link href="/" ><a className="drop-items"> REAL ESTATE </a></Link>
                    <Link href="/" ><a className="drop-items"> CONTACT </a></Link>
                </div>

            </div>
        </div>
    )
}

export default DropdownMenu
import React, { useState } from 'react'
import DropdownMenu from '../../components/DropdownMenu';
import Footer from '../../components/Footer';
import NavbarHome from '../../components/NavbarHome'
import Image from 'next/image'
import Link from 'next/link'
import SideBar from '../../components/SideBar';

export const getStaticProps = async () => {
    const res = await fetch('http://127.0.0.1:8000/London')
    const data = await res.json();

    return {
        props: { london: data }
    }
}

const LondonHome = ({ london }) => {

    const [isOpen, setIsOpen] = useState(false);

    const toggle = () => {
        setIsOpen(!isOpen);
    }
    return (
        <div>
            <NavbarHome toggle={toggle} />
            <DropdownMenu isOpen={isOpen} toggle={toggle} />
            <SideBar />
            <div id="london" className="grid mb-24 mx-4 gap-y-8 grid-cols-1 md:grid-cols-2 md:gap-x-16 lg:gap-x-8 ">
                {london.map(items => (

                    <Link href={'/London/' + items.id} key={items.id}>
                        <div className="flex mx-auto h-auto w-96 p-4 border-2 border-gray-200 rounded-xl cursor-pointer hover:shadow-xl duration-300 2xl:w-[37rem]">
                            <div className="w-2/4 2xl:w-4/12">
                                <Image width="200" height="220" className="rounded-xl object-cover " src={items.homepic} />
                            </div>
                            <div className="flex flex-col ml-3 justify-between h-48 w-2/4">
                                <h1 className="font-bold text-lg md:text-2xl 2xl:text-3xl 2xl:w-[23rem] 2xl:text-[1.5rem]">{items.address}</h1>
                                <div className="flex justify-between items-center text-gray-400">
                                    <p className="text-sm 2xl:text-lg">Post by Beluga</p>
                                    <p className="text-sm 2xl:text-lg text-white p-1 rounded-md bg-slate-400">${items.price}</p>
                                </div>
                            </div>
                        </div>
                    </Link>
                ))}
            </div>
            <Footer />
        </div>
    )
}

export default LondonHome
import React, { useState } from 'react'
import DropdownMenu from '../../components/DropdownMenu';
import Footer from '../../components/Footer';
import NavbarHome from '../../components/NavbarHome'
import Image from 'next/image'
import Link from 'next/link'
import SideBar from '../../components/SideBar';

export const getStaticProps = async () => {
    const res = await fetch('http://127.0.0.1:8000/Spain')
    const data = await res.json();

    return {
        props: { spain: data }
    }
}

const SpainHome = ({ spain }) => {

    const [isOpen, setIsOpen] = useState(false);

    const toggle = () => {
        setIsOpen(!isOpen);
    }
    return (
        <div>
            <NavbarHome toggle={toggle} />
            <DropdownMenu isOpen={isOpen} toggle={toggle} />
            <SideBar />
            <div id="spain" className="grid mb-24 mx-4 gap-y-8 grid-cols-1 md:grid-cols-2 md:gap-x-16 lg:gap-x-8 xl:px-56">
                {spain.map(items => (

                    <Link href={'/Spain/' + items.id} key={items.id}>
                        <div className="flex mx-auto h-60 w-96 p-4 border-2 border-gray-200 rounded-xl cursor-pointer hover:shadow-xl duration-300 ">
                            <div className="w-2/4">
                                <Image width="200" height="220" className="rounded-xl object-cover " src={items.homepic} />
                            </div>
                            <div className="flex flex-col ml-3 justify-between h-48 w-2/4">
                                <h1 className="font-bold text-lg md:text-2xl">{items.address}</h1>
                                <div className="flex justify-between items-center text-gray-400">
                                    <p className="text-sm">Post by Beluga</p>
                                    <p className="text-sm text-white p-1 rounded-md bg-slate-400">${items.price}</p>
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

export default SpainHome
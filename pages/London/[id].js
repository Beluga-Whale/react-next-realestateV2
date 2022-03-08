import React, { useState } from 'react'
import DropdownMenu from '../../components/DropdownMenu'
import { Carousel } from "react-bootstrap"
import NavbarHome from '../../components/NavbarHome'
import Image from 'next/image'
import Footer from '../../components/Footer'

export const getStaticPaths = async () => {
    const res = await fetch('http://127.0.0.1:8000/London')
    const data = await res.json()

    const paths = data.map(item => {
        return {
            params: { id: item.id.toString() }
        }
    })

    return {
        paths,
        fallback: false
    }

}

export const getStaticProps = async (context) => {
    const id = context.params.id;
    const res = await fetch('http://127.0.0.1:8000/London/' + id);
    const data = await res.json();

    return {
        props: { items: data }
    }
}

const DetailLondon = ({ items }) => {

    const [isOpen, setIsOpen] = useState(false);

    const toggle = () => {
        setIsOpen(!isOpen);
    }


    return (
        <div className="bg-[#e6e4e4]">

            <NavbarHome toggle={toggle} />
            <DropdownMenu isOpen={isOpen} toggle={toggle} />
            <section className="flex justify-between px-24 bg-[#0d0d0d] border-t-2 py-4 ">
                <div className="flex flex-col justify-around text-white">
                    <h1 className="font-bold text-3xl">Modern House</h1>
                    <p className="text-slate-300">{items.address}</p>
                </div>
                <div className="flex items-center text-white">
                    <h1 className="font-bold text-3xl">${items.price}</h1>
                </div>
            </section>

            <div className="my-12">
                <Carousel className="mx-auto w-[30rem] rounded-tr-3xl overflow-hidden sm:w-[33rem] lg:w-[40rem]" >
                    <Carousel.Item className="w-[30rem] lg:w-[40rem]  ">
                        <img
                            className="d-block w-100 rounded-tr-3xl"
                            src={items.images1}
                            alt="First slide"
                        />
                    </Carousel.Item>

                    <Carousel.Item className="w-[30rem] lg:w-[40rem]  ">
                        <img
                            className="d-block w-100 rounded-tr-3xl"
                            src={items.images2}
                            alt="Second slide"
                        />
                    </Carousel.Item>

                    <Carousel.Item className="w-[30rem] lg:w-[40rem]  ">
                        <img
                            className="d-block w-100 rounded-tr-3xl"
                            src={items.images3}
                            alt="Third slide"
                        />
                    </Carousel.Item>

                    <Carousel.Item className="w-[30rem] lg:w-[40rem]  ">
                        <img
                            className="d-block w-100 rounded-tr-3xl"
                            src={items.images4}
                            alt="Third slide"
                        />
                    </Carousel.Item>

                </Carousel>
            </div>

            <div className="flex mb-12 flex-col bg-white h-[9.1rem] mx-auto rounded-md w-full sm:px-12 sm:w-[37rem] lg:w-[55rem] ">
                <div className="w-full h-1/2 border-b-2 border-slate-300 p-4 font-bold text-lg sm:text-2xl ">Detail</div>
                <div className="flex justify-around items-center w-full h-1/2 ">
                    <div className="flex w-full  border-r-2">
                        <div className="flex flex-row justify-around items-center mx-auto w-20 font-bold">
                            <Image src="/bed.svg" width="16" height="16" />
                            <span>{items.bed}</span>
                        </div>
                    </div>

                    <div className="flex w-full  border-r-2">
                        <div className="flex flex-row justify-around items-center mx-auto w-20 font-bold">
                            <Image src="/bath.svg" width="16" height="16" />
                            <span>{items.baht}</span>
                        </div>
                    </div>

                    <div className="flex w-full  border-r-2">
                        <div className="flex flex-row justify-around items-center mx-auto w-20 font-bold">
                            <Image src="/livingroom.svg" width="16" height="16" />
                            <span>{items.living}</span>
                        </div>
                    </div>

                    <div className="flex w-full  border-r-2">
                        <div className="flex flex-row justify-around items-center mx-auto w-20 font-bold">
                            <Image src="/garage.svg" width="16" height="16" />
                            <span>{items.garage}</span>
                        </div>
                    </div>

                    <div className="flex w-full ">
                        <div className="flex flex-row justify-around items-center mx-auto w-20 font-bold">
                            <Image src="/date.svg" width="16" height="16" />
                            <span>{items.year}</span>
                        </div>
                    </div>
                </div>
            </div>

            <div className="mx-auto mb-24 w-full h-full bg-white rounded-lg sm:w-[37rem] lg:w-[55rem]">
                <div className="flex flex-col h-full justify-between ">
                    <div className=" text-left border-b-2 font-bold text-xl h-24">
                        <h1 className="p-7">Description</h1>
                    </div>
                    <div className="h-full p-4 ">
                        <p className="indent-9">{items.description}</p><br />
                        <p className="indent-9">{items.description2}</p>
                    </div>
                </div>
            </div>

            <Footer />
        </div>

        
    )
}

export default DetailLondon
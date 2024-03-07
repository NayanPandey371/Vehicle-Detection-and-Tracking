import Skeleton, { SkeletonTheme } from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css'

export default function Loader () {
    return (
            <SkeletonTheme baseColor='#7734e7' highlightColor="#EAE8E7">
            <p>
                <Skeleton containerClassName="flex-1" count={5} />
            </p>
            </SkeletonTheme>
      )
}
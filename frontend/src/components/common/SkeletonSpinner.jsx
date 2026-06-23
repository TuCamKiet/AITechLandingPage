export default function SkeletonSpinner() {
  return (
    <div className="col-span-full flex w-full items-center justify-center py-12">
      <div className="h-10 w-10 animate-spin rounded-full border-4 border-violet-500 border-t-transparent"></div>
    </div>
  );
}
